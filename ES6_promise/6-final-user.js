import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise
    .all([
      signUpUser(firstName, lastName).then((value) => ({ status: 'fulfilled', value })),
      uploadPhoto(fileName).then((value) => ({ status: 'fulfilled', value })),
    ])
    .catch(() => [
      { status: 'fulfilled', value: { firstName, lastName } },
      { status: 'rejected', value: new Error(`${fileName} cannot be processed`) },
    ]);
}
