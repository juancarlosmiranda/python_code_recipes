"""
    def draw_bounding_boxes_frame(img_bounding_boxes, predicted_boxes, predicted_class):
        # todo: check this variables, where put that
        rect_th = 1
        rect_solid = -1
        font_size = 2 * 0.4
        font_type = cv2.FONT_ITALIC
        text_th = 2
        selected_color = (0, 255, 0)
        size_mm = 111.12
        mass_gr = 111.12
        # message_label = f'{size_mm} mm {mass_gr} gr'
        message_label = f'{size_mm} mm'

        h_side = 5  # px

        for i in range(len(predicted_boxes)):
            print(predicted_boxes[i][0], predicted_boxes[i][1])
            print(predicted_boxes[i][2], predicted_boxes[i][3])
            class_name = message_label
            cv2.putText(img_bounding_boxes, class_name, (int(predicted_boxes[i][0]), int(predicted_boxes[i][1])),
                        font_type, font_size, selected_color,
                        thickness=text_th)
            cv2.rectangle(img_bounding_boxes, (int(predicted_boxes[i][0]), int(predicted_boxes[i][1])),
                          (int(predicted_boxes[i][2]), int(predicted_boxes[i][3])), color=selected_color,
                          thickness=rect_th)
            cv2.rectangle(img_bounding_boxes, (int(predicted_boxes[i][0]), int(predicted_boxes[i][1])),
                          (int(predicted_boxes[i][2]), int(predicted_boxes[i][1]) + h_side), color=selected_color,
                          thickness=rect_solid)

        pass
        return img_bounding_boxes

    def draw_normal_layout(img_bounding_boxes):
        W = 1920  # todo: add automatically
        H = 1080
        left_border = 10
        right_border = W - 10
        up_offset = 10
        down_offset = H - 10
        line_th = 1
        line_type = 8
        middle_w = int(W / 2)
        middle_h = int(H / 2)
        vertical_start = (middle_w, up_offset)
        vertical_end = (middle_w, down_offset)
        selected_color = (0, 255, 0)
        cv2.line(img_bounding_boxes, vertical_start, vertical_end, selected_color, line_th, line_type)

        horizontal_start = (left_border, middle_h)
        horizontal_end = (right_border, middle_h)
        cv2.line(img_bounding_boxes, horizontal_start, horizontal_end, selected_color, line_th, line_type)

        # ---------------
        total_count = 1032
        message_quantity = f'{total_count} units'
        font_type_qty = cv2.FONT_HERSHEY_PLAIN
        font_size_qty = 4
        font_th_qty = 2
        x_qty = 10
        y_qty = 100
        color_qty = (0, 255, 0)
        cv2.putText(img_bounding_boxes, message_quantity, (x_qty, y_qty), font_type_qty, font_size_qty, color_qty,
                    thickness=font_th_qty)

        # ------------------
        total_mass = 1032
        unit_selected = 'kg'
        message_quantity = f'{total_mass} {unit_selected}'
        font_type_qty = cv2.FONT_HERSHEY_PLAIN
        font_size_qty = 4
        font_th_qty = 2
        x_qty = 10
        y_qty = 150
        color_qty = (0, 255, 0)
        cv2.putText(img_bounding_boxes, message_quantity, (x_qty, y_qty), font_type_qty, font_size_qty, color_qty,
                    thickness=font_th_qty)
        # ------------------

        wide_bar_v = 15
        x1_bar_v = middle_w - wide_bar_v
        y1_bar_v = up_offset
        x2_bar_v = middle_w - wide_bar_v
        y2_bar_v = down_offset
        cv2.rectangle(img_bounding_boxes, (x1_bar_v, y1_bar_v), (x2_bar_v, y2_bar_v), color=selected_color,
                      thickness=line_th)

        wide_bar_h = 15
        x1_bar_h = left_border
        y1_bar_h = middle_h - wide_bar_h
        x2_bar_h = right_border
        y2_bar_h = middle_h + wide_bar_h
        cv2.rectangle(img_bounding_boxes, (x1_bar_h, y1_bar_h), (x2_bar_h, y2_bar_h), color=selected_color,
                      thickness=line_th)

        horizontal_start = (left_border, middle_h)
        horizontal_end = (right_border, middle_h)
        cv2.line(img_bounding_boxes, horizontal_start, horizontal_end, selected_color, line_th, line_type)

        # ----------------------
        return img_bounding_boxes
"""