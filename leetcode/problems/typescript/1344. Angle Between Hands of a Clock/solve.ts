function angleClock(hour: number, minutes: number): number {
  const minuteAngle = minutes * 6;
  const hourAngle = (hour % 12) * 30 + minutes / 2;
  const diff = Math.abs(hourAngle - minuteAngle);
  return Math.min(diff, 360 - diff);
}
