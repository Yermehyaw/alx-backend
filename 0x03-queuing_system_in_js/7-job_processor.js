/**
 * Track progress ande rrors on a job queue
 */
import { createQueue } from 'kue';

const blacklisted = [4153518780, 4153518781];

/**
 * Notifies and processes job on the push_notification_code_2 queue
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0); // set job progress to 0
  if (blacklisted.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(err);
  } else {
    job.progress(50);
    console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
  }
}

const queue = createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  console.log(`Job conatains ${job.data}`);
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
