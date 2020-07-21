var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
module.exports = {
  context: __dirname,
  entry: './static/js/index',
  output: {
    path: path.resolve('./static/webpack_bundles/'),
    filename: '[name]-[hash].js'
  },
  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' })
  ],
  module: {
    rules: [
      {
        test: /\.js|jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              '@babel/preset-react'
            ],
            plugins: ['@babel/plugin-syntax-jsx']
          }
        }
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }
}
