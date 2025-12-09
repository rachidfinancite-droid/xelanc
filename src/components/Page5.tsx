import React from 'react';

export function Page5() {
  return (
    <div className="bg-gradient-to-br from-[#151923]/80 to-[#1a1f2e]/80 backdrop-blur-sm rounded-2xl p-8 border border-white/5 shadow-2xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 bg-gradient-to-r from-amber-600 to-amber-500 rounded-2xl flex items-center justify-center text-3xl shadow-lg shadow-amber-500/30">
            📈
          </div>
          <div>
            <h2 className="text-3xl font-bold text-white mb-1">Analyste M&A</h2>
            <p className="text-gray-400 text-sm">Expertise en fusions et acquisitions</p>
          </div>
        </div>
        <div className="h-1 w-24 bg-gradient-to-r from-amber-500 to-transparent rounded-full"></div>
      </div>

      {/* Description */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Description du poste</h3>
        <p className="text-gray-300 leading-relaxed">
          L'analyste M&A conseille les entreprises dans leurs opérations de croissance externe.
          Il réalise des valorisations d'entreprises, structure les transactions, négocie avec
          les contreparties et coordonne les due diligences. Poste d'excellence en banque d'investissement.
        </p>
      </div>

      {/* Compétences Clés */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Compétences Clés</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { title: 'Valorisation', desc: 'DCF, comparables, LBO modeling', icon: '💎' },
            { title: 'Financial Modeling', desc: 'Excel avancé et modélisation complexe', icon: '📊' },
            { title: 'Due Diligence', desc: 'Analyse approfondie et risk assessment', icon: '🔍' },
            { title: 'Deal Structuring', desc: 'Montages juridiques et financiers', icon: '⚖️' },
          ].map((skill, index) => (
            <div
              key={index}
              className="bg-[#1F3A4C]/40 p-4 rounded-xl border border-amber-500/20 hover:border-amber-500/40 transition-all duration-300 hover:transform hover:scale-105"
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

      {/* Méthodologies */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Méthodologies de Valorisation</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { method: 'DCF', desc: 'Discounted Cash Flow', color: 'from-amber-500/20' },
            { method: 'Multiples', desc: 'EV/EBITDA, P/E', color: 'from-orange-500/20' },
            { method: 'LBO', desc: 'Leveraged Buyout', color: 'from-yellow-500/20' },
          ].map((item, index) => (
            <div
              key={index}
              className={`bg-gradient-to-br ${item.color} to-transparent border border-amber-500/20 rounded-xl p-5 text-center hover:border-amber-500/40 transition-all duration-300 hover:scale-105`}
            >
              <div className="text-xl font-bold text-amber-400 mb-2">{item.method}</div>
              <div className="text-sm text-gray-300">{item.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Career Path */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Parcours Type</h3>
        <div className="relative">
          <div className="absolute left-4 top-0 bottom-0 w-0.5 bg-gradient-to-b from-amber-500 to-transparent"></div>
          <div className="space-y-4">
            {[
              { level: 'Analyst', years: '0-3 ans', salary: '50-70k€' },
              { level: 'Associate', years: '3-5 ans', salary: '80-120k€' },
              { level: 'VP', years: '5-8 ans', salary: '120-200k€' },
              { level: 'Director', years: '8+ ans', salary: '200-400k€' },
            ].map((stage, index) => (
              <div key={index} className="flex items-center gap-4 pl-10">
                <div className="absolute left-2.5 w-3 h-3 bg-amber-500 rounded-full ring-4 ring-amber-500/20"></div>
                <div className="flex-1 bg-[#1a1f2e]/60 p-4 rounded-lg border border-white/5 hover:bg-[#1F3A4C]/40 transition-all duration-300">
                  <div className="flex justify-between items-center">
                    <div>
                      <div className="font-bold text-white mb-1">{stage.level}</div>
                      <div className="text-sm text-gray-400">{stage.years}</div>
                    </div>
                    <div className="text-amber-400 font-bold">{stage.salary}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Call to Action */}
      <div className="bg-gradient-to-r from-amber-600/20 to-amber-500/20 border border-amber-500/30 rounded-xl p-6 text-center">
        <h4 className="text-xl font-bold text-white mb-2">Rejoignez l'élite de la finance</h4>
        <p className="text-gray-300 mb-4">
          Formation intensive aux métiers du M&A et de la banque d'investissement
        </p>
        <button className="px-8 py-3 bg-gradient-to-r from-amber-600 to-amber-500 text-white rounded-lg font-semibold hover:shadow-xl hover:shadow-amber-500/50 transition-all duration-300 hover:scale-105">
          Bootcamp M&A
        </button>
      </div>
    </div>
  );
}
