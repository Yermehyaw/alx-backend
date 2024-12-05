/**
 * Create a redis task/Job using kue
 */

import kue from 'kue';

const data = {
  phoneNumber: '08077665544',
  message: 'Call Mr President',
};
const push_notification_code = kue.createQueue();

const job = push_notification_code.create('Job', data);

// job saved successfully
job.save((err) => {
  if (!err) {
    console.log('Notification job created: ', job.id);
  }
});

// Job completed
job.on('complete', () => console.log('Notification job completed'));

// a job on the queue failed
job.on('failed attempt', () => console.log('Notification job failed'));
