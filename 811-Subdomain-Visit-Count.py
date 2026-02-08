class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)

        for entry in cpdomains:
            visits, domain = entry.split()
            visits = int(visits)

            parts = domain.split('.')

            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                count[sub] += visits

        return [f"{v} {d}" for d, v in count.items()]
