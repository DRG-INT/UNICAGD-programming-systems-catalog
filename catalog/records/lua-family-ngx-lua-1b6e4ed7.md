# ngx_lua

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Async Runtime |
| Source type | source_list_item |
| Verification | uploaded_file |
| Canonical URL | [https://www.nginx.com/resources/wiki/modules/lua/](https://www.nginx.com/resources/wiki/modules/lua/) |
| Source record ids | lua-source-163 |

## System Engineer Summary

The core piece of OpenResty. Embeds Lua in Nginx and exposes, among other things, the cosocket API
for non-blocking sockets (compatible with LuaSocket's API).

## Operational Role

For a systems engineer, ngx_lua belongs in the Lua family inventory as part of concurrency
scheduling, I/O throughput, cancellation, and latency management.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | not_checked |
| preview/nightly | unknown |  |  | unknown | not_checked |

## Engineering Notes

- Treat category as `async_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `not_checked`.
- Preview/nightly metadata is unknown because `not_checked`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| uploaded_file |  |  | `{"kind": "uploaded_file", "source": {"file": "readme.md", "kind": "uploaded_file", "line": 163}}` |

## Evidence

Evidence records merged into this identity: `1`.

- `lua-source-163` from `master_json` as `source_list_item`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| act | Async Runtime | [open](lua-family-act-4ff0ad7b.md) |
| async | Async Runtime | [open](lua-family-async-1eb5c035.md) |
| async-framework | Async Runtime | [open](lua-family-async-framework-b849d00e.md) |
| async-utils | Async Runtime | [open](lua-family-async-utils-efc85dd0.md) |
| async.lua | Async Runtime | [open](lua-family-async-lua-668c3126.md) |
| asyncio | Async Runtime | [open](lua-family-asyncio-8daeeae9.md) |
| away-dataqueue | Async Runtime | [open](lua-family-away-dataqueue-7107fb30.md) |
| Copas | Async Runtime | [open](lua-family-copas-8a6e8951.md) |
