/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [
    './components/**/*.vue',
    './*.vue',
    './public/index.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

