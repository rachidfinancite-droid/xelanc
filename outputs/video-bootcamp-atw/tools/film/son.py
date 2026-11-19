"""Bande son : musique + percussions de synthèse calées sur les frappes (slam) et les lignes qui roulent (roll),
voix des capsules avec la musique baissée dessous, puis normalisation à −14 LUFS.
Usage : python3 son.py plan.json sortie.wav [début s] [fin s]"""
import json, sys, subprocess, os, wave
import numpy as np
SR = 48000
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
plan = json.load(open(sys.argv[1])); out = sys.argv[2]
t0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
t1 = float(sys.argv[4]) if len(sys.argv) > 4 else plan['duree']
n = int((t1 - t0) * SR)
rng = np.random.default_rng(7)

def kick(d=0.3, f0=120, f1=50, g=0.9):
    t = np.arange(int(d * SR)) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 18)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return g * np.sin(ph) * np.exp(-t * 11)
def craque(d=0.06, g=0.25):
    t = np.arange(int(d * SR)) / SR
    return g * rng.standard_normal(len(t)) * np.exp(-t * 70)
def souffle(d=0.22, g=0.10):
    x = rng.standard_normal(int(d * SR))
    k = np.linspace(0, 1, len(x)) ** 2          # montée
    x = np.convolve(x, np.ones(6) / 6, 'same')  # adoucir
    return g * x * k * np.hanning(len(x)) ** 0.3

perc = np.zeros(n)
def poser(sig, t):
    i = int((t - t0) * SR)
    if i < 0 or i >= n: return
    j = min(n, i + len(sig)); perc[i:j] += sig[:j - i]
for e in plan['events']:
    if e['type'] == 'slam':
        poser(kick(), e['t']); poser(craque(), e['t'])
    elif e['type'] == 'roll':
        poser(souffle(), e['t'] - 0.12); poser(kick(0.18, 90, 50, 0.25), e['t'])

# musique depuis le début du film, baissée sous les voix
tmp = out + '.mus.wav'
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(t0), '-t', str(t1 - t0), '-i',
                os.path.join(RACINE, 'assets', 'musique.m4a'), '-ac', '1', '-ar', str(SR), tmp], check=True)
w = wave.open(tmp); mus = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768; w.close(); os.remove(tmp)
mus = np.pad(mus, (0, max(0, n - len(mus))))[:n]
gain = np.ones(n)
voixpiste = np.zeros(n)
for e in plan['events']:
    if e['type'] != 'voix': continue
    f = os.path.join(RACINE, 'film', 'voix', e['fichier'])
    tv = out + '.v.wav'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', f, '-ac', '1', '-ar', str(SR), tv], check=True)
    w = wave.open(tv); v = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768; w.close(); os.remove(tv)
    i = int((e['t'] - t0) * SR)
    if i >= n or i + len(v) <= 0: continue
    a = max(i, 0); b = min(n, i + len(v)); voixpiste[a:b] += v[a - i:b - i] * 1.35
    r = int(0.5 * SR)  # musique à 30 % sous la voix, en rampe : la voix domine
    lo = max(0, a - r); hi = min(n, b + r)
    env = np.ones(hi - lo) * 0.30
    env[:a - lo] = np.linspace(1, 0.30, a - lo); env[len(env) - (hi - b):] = np.linspace(0.30, 1, hi - b)
    gain[lo:hi] = np.minimum(gain[lo:hi], env)
# fin : la musique monte sur le maillon ultime pour lancer le logo, continue sous l'outro, puis s'éteint en douceur
D = plan['duree']
m0 = int((D - 7 - t0) * SR); m1 = int((D - t0) * SR)
if 0 <= m0 < m1 <= n:
    gain[m0:m1] *= np.linspace(1, 1.45, m1 - m0); gain[m1:] *= 1.45
    rs = souffle(3.0, 0.07); poser(rs, D - 3.0)          # montée douce, sans impact
f0 = n - int(3.0 * SR)
if f0 > 0: gain[f0:] *= np.linspace(1, 0, n - f0) ** 1.5
pg = np.where(gain < 0.99, 0.35, 1.0)   # percussions aussi en retrait sous la voix
mix = mus * gain + perc * 0.62 * pg + voixpiste
mix = np.clip(mix, -1, 1)
raw = out + '.raw.wav'
w = wave.open(raw, 'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes()); w.close()
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', raw, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', str(SR), '-ac', '2', out], check=True)
os.remove(raw)
print('son', out, round((t1 - t0), 1), 's')
