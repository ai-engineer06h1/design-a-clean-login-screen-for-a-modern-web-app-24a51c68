# A6 QA Report

## Summary

3 passed, 2 failed (8 finding(s)), 0 skipped, 0 errored

## Dependency Vulnerabilities — PASS

No findings.

## Static Vulnerabilities — PASS

No findings.

## Hardcoded Secrets — PASS

No findings.

## Dead Code — FAIL

- **low** `api/index.py` — unused class 'User' (60% confidence)
- **low** `api/index.py` — unused function 'login' (60% confidence)
- **low** `api/index.py` — unused variable 'email' (60% confidence)
- **low** `api/index.py` — unused variable 'message' (60% confidence)
- **low** `api/index.py` — unused variable 'oauth2_scheme' (60% confidence)
- **low** `api/index.py` — unused variable 'success' (60% confidence)
- **low** `src/components/Login.jsx` — leftover console.log

## Functional / Input Validation — FAIL

- **medium** `src/components/Login.jsx` — password input with no visible format validation (pattern/regex/minLength)
