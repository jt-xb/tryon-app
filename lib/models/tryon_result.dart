// Placeholder for Tryon model classes
// Add your model classes here with Hive annotations for local storage

class TryonResult {
  final String id;
  final String originalImageUrl;
  final String tryonImageUrl;
  final DateTime createdAt;

  TryonResult({
    required this.id,
    required this.originalImageUrl,
    required this.tryonImageUrl,
    required this.createdAt,
  });
}
