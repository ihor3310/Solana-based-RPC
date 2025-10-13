# Solana-based-RPC
rpc endpoints on solana blockchain


# Solana RPC Service

## Description

A lightweight Solana RPC provider with bundle submission support (similar to Jito) and developer-friendly interface. Alternative to Helius with focus on transaction bundling capabilities and clean API design.

## API Endpoints

### RPC Methods

#### Standard JSON-RPC
**POST** `/rpc`

Standard Solana JSON-RPC methods proxy.

**Request Body:**
```python
import requests
import json

wallet_adress = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ans = requests.get(f"http://127.0.0.1:8000/rpc/{wallet_adress}")
print(ans.text)
```

**Response:** `200 OK`
```json
{"wallet_balance_in_lamports":3593272184,"wallet_balance_in_sol":3.593272184}
```

---

### Bundle Submission

#### Send Bundle
**POST** `bundles`

Submit transaction bundle for execution.

**Request Body:**
```json
{
  "transactions": ["base64_encoded_tx1", "base64_encoded_tx2"],
  "priority": "high"
}
```

**Response:** `201 Created`
```json
{
  "bundle_id": "uuid-string",
  "status": "pending",
  "created_at": "2025-09-30T12:00:00Z"
}
```

#### Get Bundle Status
**GET** `bundles/{bundle_id}`

Check bundle execution status.

**Response:** `200 OK`
```json
{
  "bundle_id": "uuid-string",
  "status": "confirmed",
  "slot": 123456,
  "transactions": ["signature1", "signature2"]
}
```
---

#### Send Transaction
**POST** `transaction`
```python
```
**Response:** `200 OK`
```json
{"signature": "5j7s6NiJS3JAkvgkoc18WVAsiSaci2pxB2A6ueCJP4tprA2TFg9wSyTLeYouxPBJEMzJinENTkpA52YStRW5Dia7", "status": "pending"}
```
---

### History

#### History check
**GET** `history`
```python
import requests
import json

key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ans = requests.get("http://127.0.0.1:8000/history/{key}")
print(ans.text)
```
#### History (delete item)
**GET** `history`
```python
import requests
import json

key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ans = requests.get("http://127.0.0.1:8000/history/{key}")
print(ans.text)
```
#### History (change notes for the last request)
**GET** `history`
```python
import requests
import json

body = {
	'id_number': 2,
	'note': 'this is my prvt rpc'
}
ans = requests.get("http://127.0.0.1:8000/history/nt", json=body)
print(ans.text)
```




### Tables

**users**
- id (UUID, PK)
- email (VARCHAR, UNIQUE)
- password_hash (VARCHAR)
- created_at (TIMESTAMP)

**api_keys**
- id (UUID, PK)
- user_id (UUID, FK -> users.id)
- key_hash (VARCHAR)
- name (VARCHAR)
- rate_limit (INTEGER)
- requests_used (INTEGER)
- created_at (TIMESTAMP)
- revoked_at (TIMESTAMP, NULL)

**bundles**
- id (UUID, PK)
- user_id (UUID, FK -> users.id)
- status (ENUM: pending/confirmed/failed)
- priority (ENUM: low/medium/high)
- slot (BIGINT, NULL)
- created_at (TIMESTAMP)
- confirmed_at (TIMESTAMP, NULL)
- fee

**transactions**
- id (UUID, PK)
- bundle_id (UUID, FK -> bundles.id)
- signature (VARCHAR)
- raw_transaction (TEXT)
- position (INTEGER)
- fee

**usage_stats**
- id (UUID, PK)
- api_key_id (UUID, FK -> api_keys.id)
- endpoint (VARCHAR)
- request_count (INTEGER)
- date (DATE)
