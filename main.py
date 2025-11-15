import math

def cluster_points(samples, num_groups, max_steps=100):
    centers = [list(p) for p in samples[:num_groups]]

    for _ in range(max_steps):
        buckets = [[] for _ in range(num_groups)]
        for pt in samples:
            dists = []
            for cen in centers:
                sq_sum = 0
                for i in range(len(pt)):
                    sq_sum += (pt[i] - cen[i]) ** 2
                dists.append(math.sqrt(sq_sum))

            nearest_idx = dists.index(min(dists))
            buckets[nearest_idx].append(pt)

        fresh_centers = []
        for idx, bucket in enumerate(buckets):
            if not bucket:                
                fresh_centers.append(centers[idx])
                continue

            dims = len(bucket[0])
            new_c = []
            for d in range(dims):
                total = sum(p[d] for p in bucket)
                new_c.append(total / len(bucket))
            fresh_centers.append(new_c)

        if fresh_centers == centers:
            break
        centers = fresh_centers

    return buckets, centers


if __name__ == "__main__":
    test_data = [
        [1, 1], [2, 1], [1, 2],
        [8, 8], [9, 8], [8, 9]
    ]

    groups, final_centers = cluster_points(test_data, num_groups=2)

    print("=== Groups ===")
    for i, g in enumerate(groups):
        print(f"Group {i}: {g}")

    print("\n=== Final Centers ===")
    for c in final_centers:
        print(c)