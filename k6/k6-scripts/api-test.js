import http from 'k6/http';
import { check, sleep, fail } from 'k6';

export const options = {
    vus: 1000000,
    duration: '10s',
}
export default function () {
    const url = 'https://prompt-lab-be-dev-uu4qhhj35a-as.a.run.app/';

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