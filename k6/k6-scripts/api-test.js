import http from 'k6/http';
import { check, sleep, fail } from 'k6';

export const options = {
    vus: 20,
    duration: '10s',
}
export default function () {
    const url = 'https://promptlab.sutmeme.com';

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.get(url, params);

    check(res, {
        'is status 200': (r) => r.status === 200,
    });
}