import React from 'react';

const App = () => {
  const spin = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/spin`);
      const data = await res.json();
      console.log(data); // or update state with result
    } catch (err) {
      console.error('Spin failed:', err);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <button
        onClick={spin}
        className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
      >
        Spin
      </button>
    </div>
  );
};

export default App;
