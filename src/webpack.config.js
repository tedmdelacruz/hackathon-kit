const path = require('path');
const webpack = require('webpack');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    mode: 'development',
    entry: {
        app: './app/web/static/src/js/app.js',
        base: './app/web/static/src/js/base.js'
    },
    output: {
        filename: '[name].min.js',
        path: path.resolve(__dirname, './app/web/static/dist')
    },
    module: {
        rules: [
          {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
          },
          {
            test: /\.vue$/,
            use: ['vue-loader']
          }
        ],
    },
    plugins: [
        new webpack.ProvidePlugin({   
            jQuery: 'jquery',
            $: 'jquery',
            jquery: 'jquery',
            Popper: ['popper.js', 'default'],
        }),
        new VueLoaderPlugin(),
    ],
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js',
        }
    }
};
