const expressSession = require('express-session');
const MemoryStore = expressSession.MemoryStore;
const crypto = require('crypto');

const SESSION_SECRET = '3df35e5dd772dd98a6feb5475d0459f8e18e08a46f48ec68234173663fca377b';
const DEVELOP_SESSION_ID = 'amwvsLiDgNHm2XXfoynBUNRA2iWoEH5E';

const store = new MemoryStore();

const sessionData = {
    cookie: {
        path: '/',
        httpOnly: true,
        maxAge: 1000 * 60 * 60 * 48
    },
    userId: 'develop'
};

store.set(DEVELOP_SESSION_ID, sessionData, (err) => {
    if (err) {
        console.error('Error setting session:', err);
        return;
    }
    
    // now generate the signed cookie
    const signature = crypto.createHmac('sha256', SESSION_SECRET)
                           .update(DEVELOP_SESSION_ID)
                           .digest('base64')
                           .replace(/\=+$/, '');
    
    const cookieValue = `s:${DEVELOP_SESSION_ID}.${signature}`;
    const encodedCookie = encodeURIComponent(cookieValue);
    
    console.log('Generated cookie:');
    console.log(`connect.sid=${encodedCookie}`);
});