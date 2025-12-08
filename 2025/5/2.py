class Span:
    def __init__(self, start, end):
        assert start <= end
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f'Span({self.start}, {self.end})'
    
    def __len__(self):
        # +1 to be inclusive, eg 5-10 would be a span of 6
        return self.end - self.start + 1
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __lt__(self, other):
        return self.start <= self.end < other.start <= other.end
    


INPUT = 'example.in'
INPUT = 'my.in'
#INPUT = 'test.in'

with open(INPUT) as file:
    lines = file.readlines()

spans = []
fresh = 0
for line in lines:
    line = line.strip()
    if '-' in line:
        # a range
        f, t = line.split('-')
        f = int(f)
        t = int(t)
        span = Span(f, t)
        if span not in spans:
            spans.append(span)
    # end if
# end for

def update_spans(_spans):
    updated_spans = _spans
    updated = False
    for outer in _spans:
        for inner in _spans:
            if outer == inner:
                continue
            elif outer < inner or inner < outer:
                continue
            else:
                # Merge
                span = Span(min(outer.start, inner.start), max(outer.end, inner.end))
                updated_spans.append(span)
                try:
                    updated_spans.remove(outer)
                except ValueError:
                    pass
                try:
                    updated_spans.remove(inner)
                except ValueError:
                    pass
                    
                updated = True
    return updated_spans, updated

updates = True
while updates:
    spans, updates = update_spans(spans)
    
sum_ = sum(len(s) for s in spans)
print(sum_)