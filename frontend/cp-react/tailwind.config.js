const colors = require('tailwindcss/colors')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      'slate': colors.slate,
      'red': colors.red,
      'orange': colors.orange,
      'yellow': colors.yellow,
      'green': colors.green,
      'blue': colors.blue,
      'navy': colors.indigo,
      'purple': colors.purple,
      'gray': colors.gray,
    },
    width: {
      20: '4.75rem',
      24: '5.75rem',
      56: '8rem',
      60: '18rem',
      72: '12rem',
      80: '24rem',
    }
  },
  plugins: [
    require('flowbite/plugin')
],
}
