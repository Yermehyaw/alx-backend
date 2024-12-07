/**
 * Tests for job creator
 */

import createPushNotificationsJobs from './8-jobs.js';
import { createQueue } from 'kue';

const queue = createQueue();

// Registering protocols for the test procedure
before(() => {
  queue.testMode.enter();
});
afterEach(() => {
  queue.testMode.clear();
});
after(() => {
  queue.testMode.exit();
});

decribe('Job creator func', () => {
  it('display a error message if jobs is not an array', () => {
    const jobData = {name: 'Boy'};

    const jobs = queue.testMode.jobs;

    //Assertions
    expect(() => createPushNotificationsJobs(jobData, queue).to.throw('Jobs is not an array'));
  });

  it('create two new jobs to the queue', () => {
    const jobData = [
      {name: 'Boy'},
      {name: 'Girl'}
    ];
    createPushNotificationsJobs(jobData, queue);

    const jobs = queue.testMode.jobs;

    expect(jobs).to.have.lengthOf(jobData.length);
  });
});
