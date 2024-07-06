/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './templates/**/*.html',
      './static/src/**/*.js',
      './portfolio/templates/**/*.html',
    ],
    theme: {
      extend: {
        fontFamily: {
            'patua': ['"Patua One"', 'sans-serif'],
            'playwrite': ['"Playwright RO"', 'sans-serif'],
          },
      },
    },

    variants: {
        extend: {},
    },

    plugins: [],
  }
  