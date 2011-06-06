import pdb
if __name__ == '__main__':
    def split_name(string, mask):
        zip_list = zip(string, mask)
        slice_list = []
        cur_slice = []
        cur_flag = mask[0]
        #pdb.set_trace()
        for l, m in zip_list:
            if m == cur_flag:
                cur_slice.append(l)
            else:
                slice_list.append((cur_slice, cur_flag))
                cur_slice = []
                cur_slice.append(l)
                cur_flag = m
        if cur_slice:
            slice_list.append((cur_slice, cur_flag))
        return [ (''.join(l_list), m) for l_list, m in slice_list ]
                
    def expand_name(namerange, mask):
        pos = namerange.rindex('\\-')
        if pos == -1:
            return [namerange]
        else:
            namerange_a = namerange[:pos]
            namerange_b = namerange[pos+2:]
            complete_list = [] # The final result list
            expand_name_range(namerange_a, namerange_b, mask, complete_list)
            return complete_list

    def expand_name_range(namerange_a, namerange_b, mask, complete_list):
        list_a = split_name(namerange_a, mask)
        list_b = split_name(namerange_b, mask)

        need_expand_list = []
        for s in range(len(list_a)):
            slice, flag = list_a[s]
            if flag == '0': # flag 0 stand by that string is an number
                differ = abs( int(slice) - int(list_b[s][0]) )
                need_expand_list.append((s, differ))
        if need_expand_list == []:
            # Save and return
            complete_list.append(namerange_a)
            return
        id, diff = max(need_expand_list, key = lambda x: x[1])
        # The id is max range to be expand.
        expand_part_list_group = expand_name_part(list_a, list_b, id)
        # Get new mask
        mask_new = ''
        for s in range(len(list_a)):
            slice, flag = list_a[s]
            if s != id:
                mask_new += flag * len(slice)
            else:
                mask_new += '1' * len(slice)
        for name_a, name_b in expand_part_list_group:
            expand_name_range(name_a, name_b, mask_new, complete_list)

    def expand_name_part(list_a, list_b, expand_id):
        def int2str(num, length):
            num = str(num)
            if len(num)<length:
                num = '%s%s' % ('0'*(length - len(num)), num)
            return num
        slice_a, flag_a = list_a[expand_id]
        slice_b, flag_b = list_b[expand_id]
        expand_len = len(slice_a)
        slice_a = int(slice_a); slice_b = int(slice_b)
        def expand_one_list(list_one):
            expand_list = []
            pre_string = ''.join([ item for item, flag in list_one[:expand_id] ])
            post_string = ''.join([ item for item, flag in list_one[expand_id+1:] ])
            rangeval = sorted((slice_a, slice_b))
            for i in range(rangeval[0], rangeval[1]+1):
                expand_list.append(pre_string + int2str(i, expand_len) + post_string)
            return expand_list
        ret = zip ( expand_one_list(list_a), expand_one_list(list_b) )
        return ret

    def videomap2list(videomap):
        videolist = []
        for video, mask in videomap:
            videolist.extend(expand_name(video, mask))
        return videolist

    videomap = [('00776\\-00778','11110'), ('00783\\-00791','11110')]

    #videomap2list(videomap)
    #print split_name('abcdefghijk', '11001100011')
    print expand_name('abc01de002f\\-abc05de009f', '11100110001')
