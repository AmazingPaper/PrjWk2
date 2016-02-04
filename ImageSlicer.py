class ImageSlicer:
	def slicePlayerDiceImages(self, image):
		result = []

		for n in range(0, 6):
			row = n // 2
			column = n % 2

			height = 280
			fullHeight = 350

			width = 560

			crop_rect = (width * column + 60 * (column + 1), fullHeight * row + 400, width, height)

			result.append(image.subsurface(crop_rect))

		return result

	def sliceSuperFighterDiceImages(self, image):
		result = []

		height = 80
		width = 660

		for n in range(0, 6):
			crop_rect = (20, 380 + n * 100, width, height)
			result.append(image.subsurface(crop_rect))

		return result

	def sliceSuperFighterImage(self, image):
		height = 344
		width = 676

		crop_rect = (14, 16, width, height)

		return image.subsurface(crop_rect)
