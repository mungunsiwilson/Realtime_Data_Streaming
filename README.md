# Realtime Data Streaming | End-to-End Data Engineering Project

## 📊 Overview
An end-to-end data engineering pipeline covering the complete data lifecycle from ingestion to storage. This project implements a robust streaming architecture using modern data engineering tools, all containerized for easy deployment and scalability.

## 🏗️ Architecture

### Pipeline Flow
1. Data Ingestion → Random user data from `randomuser.me` API
2. Orchestration → Apache Airflow workflows with PostgreSQL metadata storage
3. Streaming → Apache Kafka with Zookeeper coordination
4. Processing → Apache Spark distributed computation
5. Storage → Cassandra for processed data persistence

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Orchestration | Apache Airflow | Pipeline scheduling & workflow management |
| Metadata Storage | PostgreSQL | Airflow metadata & job tracking |
| Streaming | Apache Kafka | Real-time data streaming |
| Coordination | Apache Zookeeper | Kafka cluster coordination |
| Monitoring | Control Center & Schema Registry | Stream monitoring & schema management |
| Processing | Apache Spark | Distributed data processing |
| Storage | Cassandra | High-performance NoSQL storage |
| Development | Python | Pipeline logic & data processing |
| Containerization | Docker | Environment consistency & scalability |

## 📈 Key Features

- Complete Data Lifecycle: From ingestion to processing to storage
- Real-time Streaming: Apache Kafka for high-throughput data streaming
- Scalable Processing: Apache Spark for distributed computation
- Reliable Storage: Cassandra for time-series data persistence
- Containerized Deployment: Docker-based setup for consistent environments
- Workflow Orchestration: Apache Airflow for pipeline management
- Monitoring: Integrated monitoring with Control Center

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- Minimum 8GB RAM
- 20GB available disk space

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd realtime-data-streaming

# Start all services
docker compose up -d

# Access the services:
# Airflow UI: http://localhost:8080 (admin/admin)
# Kafka Control Center: http://localhost:9021
# Spark Master: http://localhost:9090