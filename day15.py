from utils import BaseSolver
import re


def getDistance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def getMergedSegments(segments):
    segments = sorted(segments)
    i = 0
    while i < len(segments) - 1:
        a, b = segments[i], segments[i+1]
        if a[1] >= b[0]-1:
            n = (a[0], max(a[1], b[1]))
            segments = segments[:i] + [n] + segments[i+2:]
        else:
            i += 1
    return segments


def getTrimmedSegments(segments, left, right):
    return [
        (max(left, a), min(b, right))
        for (a, b) in segments
        if b > left or a < right
    ]


class Solver(BaseSolver):

    def getInput(self, lines):
        sensorToBeacon, sensors, beacons = dict(), set(), set()
        for line in lines:
            coordinates = re.compile('-?[0-9]+').findall(line)
            coordinates = tuple(map(int, coordinates))
            sensor, beacon = coordinates[:2], coordinates[2:]
            sensorToBeacon[sensor] = (beacon, getDistance(sensor, beacon))
            sensors.add(sensor)
            beacons.add(beacon)
        return sensorToBeacon, sensors, beacons

    def getCoveredSegments(self, sensorToBeacon, y):
        segments = set()
        for sensor, (beacon, distance) in sensorToBeacon.items():
            for p in (sensor,):
                vertical = abs(p[1] - y)
                remaining = distance - vertical
                if remaining <= 0: continue
                left = p[0] - remaining
                right = p[0] + remaining
                segment = (left, right)
                segments.add(segment)
        return segments

    def run1(self, text, lines):
        target = 10
        sensorToBeacon, _, _ = self.getInput(lines)
        segments = self.getCoveredSegments(sensorToBeacon, target)
        segments = getMergedSegments(segments)
        length = sum((b-a) for a, b in segments)
        return length

    def run2(self, text, lines):
        sensorToBeacon, _, _ = self.getInput(lines)
        K = 4_000_000
        for y in range(K):
            segments = self.getCoveredSegments(sensorToBeacon, y)
            segments = getMergedSegments(segments)
            if len(segments) == 2 and segments[1][0] - segments[0][1] == 2:
                return (segments[1][0] + 1) * K + y        


Solver().solve2(sample=False)