int minOperations(char* s) {
    int i, j, k, l, m, n, o, p, q, r, t, u, v, w, x, y, z;
    int len = strlen(s);
    int cnt1 = 0, cnt2 = 0;
    for (i = 0; i < len; i++) {
        if (i % 2 == 0) {
            if (s[i] == '0') {
                cnt1++;
            } else {
                cnt2++;
            }
        } else {
            if (s[i] == '1') {
                cnt1++;
            } else {
                cnt2++;
            }
        }
    }
    return cnt1 < cnt2 ? cnt1 : cnt2;
    
}