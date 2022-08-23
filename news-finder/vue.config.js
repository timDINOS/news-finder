module.exports = {
  pages: {
    'home': {
       entry: './src/pages/Home/main.js',
       template: 'public/index.html',
       title: 'Home',
       chunks: ['chunk-vendors', 'chunk-common', 'home']
    },
    'login': {
      entry: './src/pages/Login/main.js',
      template: 'public/index.html',
      title: 'Login',
      chunks: ['chunk-vendors', 'chunk-common', 'home']
   }
  }
}
