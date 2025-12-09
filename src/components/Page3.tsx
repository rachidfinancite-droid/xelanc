import React from 'react';

export function Page3() {
  return (
    <div className="bg-gradient-to-br from-[#151923]/80 to-[#1a1f2e]/80 backdrop-blur-sm rounded-2xl p-8 border border-white/5 shadow-2xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 bg-gradient-to-r from-emerald-600 to-emerald-500 rounded-2xl flex items-center justify-center text-3xl shadow-lg shadow-emerald-500/30">
            💼
          </div>
          <div>
            <h2 className="text-3xl font-bold text-white mb-1">Chargé d'Affaires</h2>
            <p className="text-gray-400 text-sm">Développez et gérez un portefeuille clients</p>
          </div>
        </div>
        <div className="h-1 w-24 bg-gradient-to-r from-emerald-500 to-transparent rounded-full"></div>
      </div>

      {/* Description */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Description du poste</h3>
        <p className="text-gray-300 leading-relaxed">
          Le chargé d'affaires est le conseiller privilégié des entreprises. Il accompagne ses clients
          dans leurs projets de développement, finance leurs investissements et optimise leur trésorerie.
          Véritable commercial, il développe également son portefeuille par la prospection.
        </p>
      </div>

      {/* Compétences Clés */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Compétences Clés</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { title: 'Relation Client', desc: 'Développement et fidélisation du portefeuille', icon: '🤝' },
            { title: 'Analyse d\'Affaires', desc: 'Compréhension des besoins et solutions adaptées', icon: '🎯' },
            { title: 'Produits Bancaires', desc: 'Maîtrise complète de l\'offre entreprise', icon: '🏦' },
            { title: 'Négociation', desc: 'Techniques de vente et closing commercial', icon: '💬' },
          ].map((skill, index) => (
            <div
              key={index}
              className="bg-[#1F3A4C]/40 p-4 rounded-xl border border-emerald-500/20 hover:border-emerald-500/40 transition-all duration-300 hover:transform hover:scale-105"
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

      {/* Stats */}
      <div className="grid grid-cols-3 gap-4 mb-8">
        {[
          { label: 'Salaire Moyen', value: '45-65k€', icon: '💰' },
          { label: 'Embauches/an', value: '3,500+', icon: '👥' },
          { label: 'Évolution', value: 'Rapide', icon: '📈' },
        ].map((stat, index) => (
          <div key={index} className="bg-gradient-to-br from-emerald-500/10 to-emerald-600/10 border border-emerald-500/20 rounded-xl p-4 text-center">
            <div className="text-2xl mb-2">{stat.icon}</div>
            <div className="text-2xl font-bold text-emerald-400 mb-1">{stat.value}</div>
            <div className="text-xs text-gray-400">{stat.label}</div>
          </div>
        ))}
      </div>

      {/* Call to Action */}
      <div className="bg-gradient-to-r from-emerald-600/20 to-emerald-500/20 border border-emerald-500/30 rounded-xl p-6 text-center">
        <h4 className="text-xl font-bold text-white mb-2">Lancez votre carrière de Chargé d'Affaires</h4>
        <p className="text-gray-300 mb-4">
          Formation complète de la prospection à la gestion de portefeuille
        </p>
        <button className="px-8 py-3 bg-gradient-to-r from-emerald-600 to-emerald-500 text-white rounded-lg font-semibold hover:shadow-xl hover:shadow-emerald-500/50 transition-all duration-300 hover:scale-105">
          Découvrir le parcours
        </button>
      </div>
    </div>
  );
}
