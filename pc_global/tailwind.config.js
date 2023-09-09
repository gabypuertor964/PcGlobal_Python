/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',

    './landing/templates/**/*.html',
    './landing/templates/**/**/*.html',
    './landing/templates/**/**/**/*.html',

    './authentication/templates/**/*.html',
    './authentication/templates/**/**/*.html',
    './authentication/templates/**/**/**/*.html',

    './facturation/templates/**/*.html',
    './facturation/templates/**/**/*.html',
    './facturation/templates/**/**/**/*.html',

    './pqrs/templates/**/*.html',
    './pqrs/templates/**/**/*.html',
    './pqrs/templates/**/**/**/*.html',

    './inventory/templates/**/*.html',
    './inventory/templates/**/**/*.html',
    './inventory/templates/**/**/**/*.html',

    
    './carts/templates/**/*.html',
    './carts/templates/**/**/*.html',
    './carts/templates/**/**/**/*.html',
    './carts/templates/**/**/**/**/*.html',
    './carts/templates/**/**/**/**/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [ require('@tailwindcss/typography'),],
}

