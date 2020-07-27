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

module.exports = [{
  entry: '../app.scss',
  output: {
    // This is necessary for webpack to compile
    // But we never use style-bundle.js
    filename: 'style-bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'bundle.css'
            }
          },
          { loader: 'extract-loader' },
          { loader: 'css-loader' },
          {
            loader: 'sass-loader',
            options: {
              // Prefer Dart Sass
              implementation: require('sass'),

              // See https://github.com/webpack-contrib/sass-loader/issues/804
              webpackImporter: false
            }
          }
        ]
      }
    ]
  }
}]
