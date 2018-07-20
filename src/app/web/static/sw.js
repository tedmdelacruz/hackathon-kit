importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.3.1/workbox-sw.js');

workbox.routing.registerRoute(
  '/#/',
  workbox.strategies.networkFirst({
    cacheName: 'index',
  }),
);

// https://developers.google.com/web/tools/workbox/guides/common-recipes
workbox.routing.registerRoute(
  /\.(?:js|css)$/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: 'static-resources',
  }),
);
