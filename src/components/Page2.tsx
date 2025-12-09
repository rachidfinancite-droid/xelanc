import React from 'react';

export function Page2() {
  return (
    <div className="bg-gradient-to-br from-[#151923]/80 to-[#1a1f2e]/80 backdrop-blur-sm rounded-2xl p-8 border border-white/5 shadow-2xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 bg-gradient-to-r from-blue-600 to-blue-500 rounded-2xl flex items-center justify-center text-3xl shadow-lg shadow-blue-500/30">
            📊
          </div>
          <div>
            <h2 className="text-3xl font-bold text-white mb-1">Analyste Crédit</h2>
            <p className="text-gray-400 text-sm">Évaluez et gérez les risques de crédit</p>
          </div>
        </div>
        <div className="h-1 w-24 bg-gradient-to-r from-blue-500 to-transparent rounded-full"></div>
      </div>

      {/* Description */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Description du poste</h3>
        <p className="text-gray-300 leading-relaxed">
          L'analyste crédit joue un rôle crucial dans l'évaluation de la solvabilité des clients
          et la gestion des risques financiers. Ce professionnel examine les états financiers,
          analyse les tendances du marché et élabore des recommandations pour les décisions de crédit.
        </p>
      </div>

      {/* Compétences Clés */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Compétences Clés</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { title: 'Analyse Financière', desc: 'Maîtrise des ratios et indicateurs financiers', icon: '📈' },
            { title: 'Évaluation des Risques', desc: 'Identification et quantification des risques', icon: '⚠️' },
            { title: 'Réglementation Bancaire', desc: 'Connaissance de Bâle III et normes prudentielles', icon: '📋' },
            { title: 'Outils Analytics', desc: 'Excel, SAS, Python pour modélisation', icon: '💻' },
          ].map((skill, index) => (
            <div
              key={index}
              className="bg-[#1F3A4C]/40 p-4 rounded-xl border border-blue-500/20 hover:border-blue-500/40 transition-all duration-300 hover:transform hover:scale-105"
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

      {/* Parcours de Formation */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold text-white mb-4">Parcours de Formation Recommandé</h3>
        <div className="space-y-3">
          {[
            { level: 'Débutant', course: 'Fondamentaux de l\'Analyse Crédit', duration: '15h', price: '199€' },
            { level: 'Intermédiaire', course: 'Modélisation des Risques de Crédit', duration: '24h', price: '299€' },
            { level: 'Avancé', course: 'Credit Portfolio Management', duration: '32h', price: '399€' },
          ].map((item, index) => (
            <div
              key={index}
              className="flex items-center justify-between p-4 bg-[#1a1f2e]/60 rounded-lg border border-white/5 hover:bg-[#1F3A4C]/40 transition-all duration-300"
            >
              <div className="flex items-center gap-4">
                <div className="w-10 h-10 bg-blue-500/20 rounded-lg flex items-center justify-center text-blue-400 font-bold">
                  {index + 1}
                </div>
                <div>
                  <div className="text-xs text-blue-400 font-semibold mb-1">{item.level}</div>
                  <div className="text-white font-medium">{item.course}</div>
                </div>
              </div>
              <div className="flex items-center gap-6">
                <div className="text-gray-400 text-sm">⏱️ {item.duration}</div>
                <div className="text-blue-400 font-bold">{item.price}</div>
                <button className="px-4 py-2 bg-gradient-to-r from-blue-600 to-blue-500 text-white rounded-lg text-sm font-semibold hover:shadow-lg hover:shadow-blue-500/30 transition-all duration-300 hover:scale-105">
                  Commencer
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Call to Action */}
      <div className="bg-gradient-to-r from-blue-600/20 to-blue-500/20 border border-blue-500/30 rounded-xl p-6 text-center">
        <h4 className="text-xl font-bold text-white mb-2">Prêt à devenir Analyste Crédit ?</h4>
        <p className="text-gray-300 mb-4">
          Rejoignez plus de 1,200 professionnels qui ont transformé leur carrière
        </p>
        <button className="px-8 py-3 bg-gradient-to-r from-blue-600 to-blue-500 text-white rounded-lg font-semibold hover:shadow-xl hover:shadow-blue-500/50 transition-all duration-300 hover:scale-105">
          Voir tous les cours
        </button>
      </div>
    </div>
  );
}
