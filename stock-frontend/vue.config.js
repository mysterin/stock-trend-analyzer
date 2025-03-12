const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    hot: true,
    port: 7000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      }
    },
    allowedHosts: [
      'localhost',
      'mysterin.xicp.net'
    ]
  }
})
