import React from 'react';

export function Page4() {
  return (
    <div className="bg-gradient-to-br from-[#151923]/80 to-[#1a1f2e]/80 backdrop-blur-sm rounded-2xl p-8 border border-white/5 shadow-2xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 bg-gradient-to-r from-purple-600 to-purple-500 rounded-2xl flex items-center justify-center text-3xl shadow-lg shadow-purple-500/30">
            🏦
          </div>
          <div>
            <h2 className="text-3xl font-bold text-white mb-1">Directeur d'Agence</h2>
            <p className="text-gray-400 text-sm">Pilotez la performance et managez les équipes</p>
          </div>
        </div>
        <div className="h-1 w-24 bg-gradient-to-r from-purple-500 to-transparent rounded-full"></div>
      </div>

      {/* Description */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Description du poste</h3>
        <p className="text-gray-300 leading-relaxed">
          Le directeur d'agence bancaire assure le développement commercial et la gestion opérationnelle
          de son point de vente. Manager confirmé, il anime ses équipes, définit la stratégie locale
          et garantit l'atteinte des objectifs tout en veillant à la satisfaction client.
        </p>
      </div>

      {/* Compétences Clés */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Compétences Clés</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { title: 'Leadership', desc: 'Animation et motivation des équipes', icon: '👔' },
            { title: 'Gestion P&L', desc: 'Pilotage de la performance financière', icon: '📊' },
            { title: 'Stratégie Commerciale', desc: 'Développement du CA et parts de marché', icon: '🎯' },
            { title: 'Risk Management', desc: 'Contrôle des risques et conformité', icon: '🛡️' },
          ].map((skill, index) => (
            <div
              key={index}
              className="bg-[#1F3A4C]/40 p-4 rounded-xl border border-purple-500/20 hover:border-purple-500/40 transition-all duration-300 hover:transform hover:scale-105"
            >
              <div className="flex items-start gap-3">
                <span className="text-2xl" role="img" aria-hidden="true">{skill.icon}</span>
                <div>
                  <h4 className="font-semibold text-white mb-1">{skill.title}</h4>
                  <p className="text-gray-400 text-sm">{skill.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Responsabilités */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Responsabilités Principales</h3>
        <div className="space-y-3">
          {[
            'Management et développement de 5 à 15 collaborateurs',
            'Pilotage du budget et des objectifs commerciaux',
            'Gestion des grands comptes et clients stratégiques',
            'Conformité réglementaire et contrôle des risques',
            'Représentation de la banque auprès des acteurs locaux',
          ].map((resp, index) => (
            <div
              key={index}
              className="flex items-center gap-3 p-3 bg-[#1a1f2e]/60 rounded-lg border border-white/5 hover:bg-[#1F3A4C]/40 transition-all duration-300"
            >
              <div className="w-6 h-6 bg-purple-500/20 rounded-full flex items-center justify-center text-purple-400 text-xs font-bold flex-shrink-0">
                ✓
              </div>
              <span className="text-gray-300">{resp}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Call to Action */}
      <div className="bg-gradient-to-r from-purple-600/20 to-purple-500/20 border border-purple-500/30 rounded-xl p-6 text-center">
        <h4 className="text-xl font-bold text-white mb-2">Accédez aux fonctions de Direction</h4>
        <p className="text-gray-300 mb-4">
          Formation executive en management bancaire et pilotage d'agence
        </p>
        <button className="px-8 py-3 bg-gradient-to-r from-purple-600 to-purple-500 text-white rounded-lg font-semibold hover:shadow-xl hover:shadow-purple-500/50 transition-all duration-300 hover:scale-105">
          Programme Executive
        </button>
      </div>
    </div>
  );
}
