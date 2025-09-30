# Solana-based-RPC
RPC endpoints on Solana blockchain


# Solana RPC Service

## Description

A lightweight Solana RPC provider with developer-friendly interface. Alternative to Helius with focus on transaction bundling capabilities and clean API design.

## API Endpoints

### RPC Methods

#### Standard JSON-RPC
**POST** `/api/info`

Standard Solana JSON-RPC.

**Request Body:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "getBalance",
  "params": ["7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU"]
}
```

**Response:** `200 OK`
```json
{
  "jsonrpc": "2.0",
  "result": {
    "context": {"slot": 123456},
    "value": 500000000
  },
  "id": 1
}
```

---

### Bundle Submission

#### Submit Bundle
**POST** `/api/bundles`

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
**GET** `/api/bundles/{bundle_id}`

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
