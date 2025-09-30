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
**POST** `/api/v1/bundles`

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
**GET** `/api/v1/bundles/{bundle_id}`

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

#### List Bundles
**GET** `/api/v1/bundles?limit=10&offset=0`

Get user's bundle history.

**Query Parameters:**
- `limit` (optional, default: 10)
- `offset` (optional, default: 0)
- `status` (optional: pending/confirmed/failed)

**Response:** `200 OK`
```json
{
  "bundles": [
    {
      "bundle_id": "uuid",
      "status": "confirmed",
      "created_at": "2025-09-30T12:00:00Z"
    }
  ],
  "total": 25
}
```

---

### API Key Management

#### Create API Key
**POST** `/api/v1/keys`

Generate new API key.

**Request Body:**
```json
{
  "name": "My Project Key",
  "rate_limit": 1000
}
```

**Response:** `201 Created`
```json
{
  "key_id": "uuid",
  "api_key": "sk_live_xxxxxx",
  "name": "My Project Key",
  "rate_limit": 1000,
  "created_at": "2025-09-30T12:00:00Z"
}
```

#### List API Keys
**GET** `/api/v1/keys`

Get all API keys for user.

**Response:** `200 OK`
```json
{
  "keys": [
    {
      "key_id": "uuid",
      "name": "My Project Key",
      "rate_limit": 1000,
      "requests_used": 450,
      "created_at": "2025-09-30T12:00:00Z"
    }
  ]
}
```

#### Delete API Key
**DELETE** `/api/v1/keys/{key_id}`

Revoke API key.

**Response:** `204 No Content`

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
