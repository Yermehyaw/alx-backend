/**
 * A job creating function
 */

function createPushNotificationsJobs(jobs, queue) {
  if (!job.isArray()) {
    throw new Error('Jobs is not an array');
  }

  for (const jobData of jobs) {
    job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (!err) {
	console.log('Notification job created: ', job.id);
      }
      job.on('complete', () => console.log(`Notification job ${job.id} completed`));
      job.on('failed attempt', (err) => console.log(`Notification job ${job.id} failed: ${err}`));
      job,on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
  }
}

export default createPushNotificationsJobs;
