// service-worker.js
const blobMap = new Map();

self.addEventListener('message', (event) => {
    if (event.data.type === 'SET_BLOB') {
        blobMap.set(event.data.filename, event.data.blob);
    }
});

self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);
    const filename = url.pathname.split('/').pop();

    if (blobMap.has(filename)) {
        event.respondWith(
            new Response(blobMap.get(filename), {
                headers: { 'Content-Type': 'application/octet-stream' }
            })
        );
    }
});

self.addEventListener('activate', event => event.waitUntil(clients.claim()));