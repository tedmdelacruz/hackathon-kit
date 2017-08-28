const path = require('path');
const webpack = require('webpack');


module.exports = {
    entry: './web/static/src/js/app.js',
    output: {
        filename: 'app.min.js',
        path: path.resolve(__dirname, 'web/static/dist')
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
    ],
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js',
        }
    }
};
