importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.3.1/workbox-sw.js');

// Assets
// https://developers.google.com/web/tools/workbox/guides/common-recipes
workbox.routing.registerRoute(
  /\.(?:js|css)$/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: 'static-resources',
  }),
);

// App-specific
workbox.routing.registerRoute(
  '/#/',
  workbox.strategies.cacheFirst({
    cacheName: 'index',
  }),
);

workbox.routing.registerRoute(
  '/api/users/',
  workbox.strategies.networkFirst({
    cacheName: 'users',
  }),
);