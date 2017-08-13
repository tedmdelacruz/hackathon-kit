const path = require('path');
const webpack = require('webpack');


module.exports = {
    entry: './src/js/app.js',
    output: {
        filename: 'app.min.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
          {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
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
