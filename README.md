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

### Transaction Submission

#### Send Transaction
**POST** `/api/transaction`

Submit single transaction for execution.

**Request Body:**
```json
{
  "transaction": "base64_encoded_transaction",
  "priority": "medium"
}
```

**Response:** `201 Created`
```json
{
  "signature": "5j7s6NiJS3JAkvgkoc18WVAsiSaci2pxB2A6ueCJP4tprA2TFg9wSyTLeYouxPBJEMzJinENTkpA52YStRW5Dia7",
  "status": "pending"
}
```

---

### Tables

**bundles**
- bundle_id (VARCHAR, UNIQUE)
- status (ENUM: pending/confirmed/failed)
- priority (ENUM: low/medium/high)
- slot (BIGINT, NULL)
- fee (DECIMAL)
- created_at (TIMESTAMP)
- confirmed_at (TIMESTAMP, NULL)

**transactions**
- bundle_id (VARCHAR, FK -> bundles.bundle_id)
- signature (VARCHAR)
- position (INTEGER)
- fee (DECIMAL)
