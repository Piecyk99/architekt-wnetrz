import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // Modern Polish Apartment palette
        walnut: {
          50: "#faf6f1",
          100: "#f0e4d3",
          200: "#dbc09a",
          300: "#c29b6b",
          400: "#a87a4a",
          500: "#8b6037",
          600: "#6b4828",
          700: "#4d331c",
          800: "#332113",
          900: "#1f140a",
        },
        cream: {
          50: "#fdfbf7",
          100: "#f6efe1",
          200: "#ede0c4",
        },
      },
      fontFamily: {
        sans: ["system-ui", "-apple-system", "Segoe UI", "Roboto", "Helvetica Neue", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
