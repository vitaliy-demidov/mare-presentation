// Self-destructing Service Worker: purge all caches and unregister
self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(keys.map((k) => caches.delete(k)));
    }).then(() => self.clients.claim()).then(() => {
      return self.registration.unregister();
    })
  );
});

self.addEventListener('fetch', (e) => {
  // Always fetch directly from network, no caching
  return;
});
