# Redis Queuing System Project

## Description

This project demonstrates the use of Redis for managing a queuing system in JavaScript. It includes various Redis operations, both synchronous and asynchronous, for managing jobs in a queue.

## Project Structure

```bash
   /home/eddy/alx/alx-backend/0x03-queuing_system_in_js │ -0-redis_client.js # Basic Redis client setup - 1-redis_op.js # Basic Redis operations - 2-redis_op_async.js # Asynchronous Redis operations - 4-redis_advanced_op.js # Advanced Redis operations - 5-publisher.js # Job publisher - 5-subscriber.js # Job subscriber - 6-job_creator.js # Job creator - 6-job_processor.js # Job processor - 7-job_creator.js # Enhanced job creator - 7-job_processor.js # Enhanced job processor - 8-job.js # Job management - 8-job.test.js # Unit tests for jobs - 9-stock.js # Stock management - dump.rdb # Redis data dump - package.json # Project dependencies and scripts - package-lock.json # Exact versioning of installed packages

## Author
   Edwin Kambale

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo/0x03-queuing_system_in_js
Install dependencies
   npm install

## Usage
sudo systemctl start redis
`To run the application
node 0-redis_client.js