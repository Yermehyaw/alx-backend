/**
 * Create a running client to connect to a running backgrpund server 
 * inorder to store and retrieve data
 */

import redis from 'redis';
import { promisify } from 'util';


/**
 * set values on he client
 */
function setNewSchool(schoolName, value) {
  const client = redis.createClient();
  client.on('error', err => console.log('Redis client not connected to the server: ', err));

  client.on('connect', () => console.log('Redis client connected to the server'));

  client.on('ready', () => {
    client.set(schoolName, value, redis.print);
  });
}


/**
 * Get the value of a key in the db
 */
async function displaySchoolValue(schoolName) {
  try {
    const client = redis.createClient();
    const getAsync = promisify(client.get).bind(client);

    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.log('Redis client not connected to the server: ', error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
