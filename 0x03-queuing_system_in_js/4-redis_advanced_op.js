/**
 * Create a running client to connect to a running backgrpund server 
 * inorder to store and retrieve hash data
 */

import redis from 'redis';

const client = redis.createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('ready', () => {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);

  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log('Err retrieving hashing values: ', err);
      return;
    }
    console.log(reply);
  });
});
