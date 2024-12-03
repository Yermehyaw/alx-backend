/**
 * Create a running client to connect to a running backgrpund server 
 * inorder to store and retrieve data
 */

import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

// await client.connect();
