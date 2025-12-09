import React, { useState } from 'react';
import { Page2 } from './components/Page2';
import { Page3 } from './components/Page3';
import { Page4 } from './components/Page4';
import { Page5 } from './components/Page5';

type PageId = 2 | 3 | 4 | 5;

interface NavigationTab {
  id: PageId;
  label: string;
  icon: string;
  component: React.ComponentType;
}

const NAVIGATION_TABS: NavigationTab[] = [
  { id: 2, label: 'Analyste Crédit', icon: '📊', component: Page2 },
  { id: 3, label: 'Chargé d\'Affaires', icon: '💼', component: Page3 },
  { id: 4, label: 'Directeur d\'Agence', icon: '🏦', component: Page4 },
  { id: 5, label: 'Analyste M&A', icon: '📈', component: Page5 },
];

export default function App() {
  const [currentPage, setCurrentPage] = useState<PageId>(2);

  const CurrentPageComponent = NAVIGATION_TABS.find(tab => tab.id === currentPage)?.component || Page2;

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0a0e1a] via-[#0d0d0d] to-[#0a1628] flex flex-col items-center justify-center p-6 md:p-10">
      {/* Navigation Container */}
      <div className="w-full max-w-6xl mb-8">
        {/* Navigation Header */}
        <div className="text-center mb-6">
          <h1 className="text-white text-2xl md:text-3xl font-bold mb-2 tracking-tight">
            Parcours Professionnels
          </h1>
          <p className="text-gray-400 text-sm md:text-base">
            Sélectionnez votre spécialisation en finance bancaire
          </p>
        </div>

        {/* Navigation Tabs */}
        <nav className="relative bg-[#151923]/50 backdrop-blur-sm rounded-2xl p-2 border border-white/5 shadow-2xl">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
            {NAVIGATION_TABS.map(({ id, label, icon }) => (
              <button
                key={id}
                onClick={() => setCurrentPage(id)}
                className={`
                  group relative px-4 py-4 md:py-3.5 rounded-xl
                  transition-all duration-300 ease-out
                  overflow-hidden
                  ${currentPage === id
                    ? 'bg-gradient-to-r from-blue-600 to-blue-500 text-white shadow-lg shadow-blue-500/30'
                    : 'bg-[#1a1f2e]/60 text-gray-300 hover:bg-[#1F3A4C]/80 hover:text-white'
                  }
                `}
                aria-current={currentPage === id ? 'page' : undefined}
              >
                {/* Hover Glow Effect */}
                <div className={`
                  absolute inset-0 bg-gradient-to-r from-blue-400/20 to-blue-600/20
                  opacity-0 group-hover:opacity-100 transition-opacity duration-300
                  ${currentPage === id ? 'opacity-0' : ''}
                `} />

                {/* Content */}
                <div className="relative flex flex-col md:flex-row items-center justify-center gap-2">
                  <span className="text-2xl md:text-xl" role="img" aria-hidden="true">
                    {icon}
                  </span>
                  <span className="font-semibold text-xs md:text-sm tracking-wide text-center md:text-left">
                    {label}
                  </span>
                </div>

                {/* Active Indicator */}
                {currentPage === id && (
                  <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-1/3 h-1 bg-white rounded-full shadow-lg shadow-white/50" />
                )}

                {/* Ripple Effect on Click */}
                <div className={`
                  absolute inset-0 rounded-xl
                  transition-transform duration-500 ease-out
                  ${currentPage === id ? 'scale-0' : 'scale-100'}
                  bg-white/10
                `} />
              </button>
            ))}
          </div>

          {/* Animated Background Slider */}
          <div
            className="absolute top-2 h-[calc(100%-1rem)] bg-gradient-to-r from-blue-600/30 to-blue-500/30 rounded-xl transition-all duration-500 ease-out pointer-events-none hidden md:block"
            style={{
              width: `calc(25% - 0.5rem)`,
              left: `calc(${(NAVIGATION_TABS.findIndex(t => t.id === currentPage) * 25)}% + 0.5rem)`,
            }}
          />
        </nav>

        {/* Progress Indicator */}
        <div className="flex items-center justify-center gap-2 mt-4">
          {NAVIGATION_TABS.map(({ id }) => (
            <div
              key={id}
              className={`
                h-1.5 rounded-full transition-all duration-300
                ${currentPage === id
                  ? 'w-12 bg-gradient-to-r from-blue-500 to-blue-400 shadow-lg shadow-blue-500/50'
                  : 'w-1.5 bg-gray-600/50'
                }
              `}
            />
          ))}
        </div>
      </div>

      {/* Page Content with Transition */}
      <div className="w-full max-w-7xl">
        <div className="animate-fadeIn">
          <CurrentPageComponent />
        </div>
      </div>

      {/* Custom Animations */}
      <style jsx>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fadeIn {
          animation: fadeIn 0.4s ease-out;
        }
      `}</style>
    </div>
  );
}
