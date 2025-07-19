import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [vue()],
//   server: {
//     // port: # add port
//   },
//   base: '/static/',
//   resolve: {
//     alias: {
//       '@': path.resolve(__dirname, './src')
//     }
//   }
// })


// OLD
export default defineConfig({
  plugins: [vue()],
  server: {
    // port: # add port
  },
  build: {
    rollupOptions: {
      input: {
        main: "./src/main.js"
      },
      output: {
        dir: "../server/static/vue/",
        entryFileNames: '[name].js'
      }
    }
  }
})
