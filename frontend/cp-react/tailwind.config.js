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
  },
  plugins: [
    require('flowbite/plugin')
],
}
