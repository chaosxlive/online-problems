function jump(nums: number[]): number {
  const N = nums.length;
  if (N <= 1) {
    return 0;
  }

  let steps = 1;
  let farthest = 0;
  let checkEnd = 0;

  for (let i = 0; i < N - 1; i++) {
    farthest = Math.max(i + nums[i], farthest);
    if (farthest >= N - 1) {
      break;
    }
    if (i == checkEnd) {
      steps += 1;
      checkEnd = farthest;
    }
  }
  return steps;
}
